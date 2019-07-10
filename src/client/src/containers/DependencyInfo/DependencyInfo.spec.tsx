import * as React from "react";
import { shallow } from "enzyme";
import { WIZARD_CONTENT_INTERNAL_NAMES } from "../../utils/constants";
import DependencyInfo, { dependencies } from "./index";
import { ReactComponent as Warning } from "../../assets/warning.svg";
import { ReactComponent as Checkmark } from "../../assets/checkgreen.svg";

describe("DependencyInfo", () => {
  let props: any;
  let wrapper: any;
  let mockDependenciesStore = {
    dependencies: {
      node: {
        installed: true
      },
      python: {
        installed: false
      }
    }
  };

  // const dependencyMessageInstalled: string = intl.formatMessage(
  //   messages.installed,
  //   {
  //     dependencyName: WIZARD_CONTENT_INTERNAL_NAMES.FLASK
  //   }
  // );

  beforeEach(() => {
    props = {
      dependenciesStore: mockDependenciesStore,
      frameworkName: WIZARD_CONTENT_INTERNAL_NAMES.FLASK,
      intl: global.intl
    };
    wrapper = shallow(<DependencyInfo {...props} />);
  });

  it("renders without crashing", () => {
    expect(wrapper).toBeDefined();
  });

  it("is a button div", () => {
    expect(wrapper.at(0).is("button"));
  });

  it("has an image div", () => {
    const imgDiv = wrapper.at(0).at(0);
    expect(imgDiv.is("img"));
  });
});
